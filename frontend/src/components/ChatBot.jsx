import { useState, useEffect, useRef } from "react";
import ChatMessage from "./ChatMessage";


function ChatBot({sessionId, refreshSessions}) {

    const [message, setMessage] = useState("");
    const [chat, setChat] = useState([]);
    const [loading, setLoading] = useState(false);

    const chatEndRef = useRef(null);


useEffect(() => {
    const loadHistory = async () => {
        const response = await fetch(
            `http://127.0.0.1:8000/history/${sessionId}`
        );

        const data = await response.json();

        setChat(data.history);
    };

    loadHistory();
}, [sessionId]);

useEffect (() => {
    chatEndRef.current?.scrollIntoView({
        behavior: "smooth"
    })
}, [chat, loading])

    const sendMessage = async () => {
    if (!message.trim()) return;

    const userMessage = message;

    // Add the user message
    setChat(prev => [
        ...prev,
        { role: "user", message: userMessage }
    ]);

    // Clear the input immediately
    setMessage("");

    try {
        setLoading(true);

        const response = await fetch("http://127.0.0.1:8000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                question: userMessage,
                session_id: sessionId
            })
        });

        console.log("Status:", response.status);

        const data = await response.json();

        setChat(prev => [
            ...prev,
            { role: "assistant", message: data.answer }
        ]);

        await refreshSessions();

        setLoading(false);

    } catch (error) {
        console.error("Error:", error);
        setLoading(false);
    }
};

   return (
    <div>


        <div className="chat-container">
            {chat.map((msg, index) => (
                    <ChatMessage
                        key={index}
                        role={msg.role}
                        message={msg.message}
                    />
                )
            )}
            {loading && (
                <p>🤖 Assistant is typing</p>
            )}

            <div ref={chatEndRef} />
        </div>

        <div className="input-area">
            <input
                value={message}
                placeholder="Ask a question..."
                onChange={(e) => setMessage(e.target.value)}
                onKeyDown={(e) => {
                    if (e.key === "Enter") {
                        sendMessage();
                    }
                }}
            />

            <button onClick={sendMessage}>
                Send
            </button>
        </div>
    </div>
);
}

export default ChatBot;