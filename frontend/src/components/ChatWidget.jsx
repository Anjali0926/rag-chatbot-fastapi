import { useState } from "react";
import { FaRobot, FaTimes } from "react-icons/fa";
import ChatBot from "./ChatBot";
import Sidebar from "./Sidebar";

function ChatWidget({
    sessionId,
    refreshSessions,
    onNewChat,
    sessions,
    selectedSession,
    onSelectSession
}) {

    const [open, setOpen] = useState(false);
    const [showHistory, setShowHistory] = useState(false);

    return (
        <>

            <button
                onClick={() => setOpen(!open)}
                className="fixed bottom-6 right-6 w-16 h-16 bg-blue-600 text-white rounded-full shadow-xl hover:bg-blue-700 transition flex items-center justify-center text-2xl z-50"
            >
                {open ? <FaTimes /> : <FaRobot />}
            </button>

            {open && (

                <div className="fixed bottom-24 right-6 w-[420px] h-[650px] bg-white rounded-2xl shadow-2xl overflow-hidden border z-40">

                    <div className="bg-blue-600 text-white px-5 py-4 flex justify-between items-center">

                        <h2 className="font-bold text-lg flex items-center gap-2">
                            🤖 ABC AI Assistant
                        </h2>

                        <div className="flex items-center gap-2">

                            <button
                                onClick={() =>
                                    setShowHistory(!showHistory)
                                }
                                className="bg-white text-blue-600 px-3 py-1 rounded-md text-sm font-medium hover:bg-gray-100 transition"
                            >
                                History
                            </button>

                            <button
                                onClick={onNewChat}
                                className="bg-white text-blue-600 px-3 py-1 rounded-md text-sm font-medium hover:bg-gray-100 transition"
                            >
                                + New Chat
                            </button>

                        </div>

                    </div>

                    <div className="h-[calc(100%-72px)] overflow-hidden">

                        {showHistory ? (

                            <div className="p-4">

                                <Sidebar
                                    sessions={sessions}
                                    selectedSession={selectedSession}
                                    onSelectSession={(sessionId) => {
                                        onSelectSession(sessionId);
                                        setShowHistory(false);
                                    }}
                                    onNewChat={() => {
                                        onNewChat();
                                        setShowHistory(false);
                                    }}
                                    onClose={() =>
                                        setShowHistory(false)
                                    }
                                />

                            </div>

                        ) : (

                            <ChatBot
                                sessionId={sessionId}
                                refreshSessions={refreshSessions}
                            />

                        )}

                    </div>

                </div>

            )}

        </>
    );
}

export default ChatWidget;