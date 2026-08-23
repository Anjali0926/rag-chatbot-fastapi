function ChatMessage({ role, message }) {
  const isUser = role === "user";

  return (
    <div className={`flex ${isUser ? "justify-end" : "justify-start"} mb-4`}>
      <div
        className={`max-w-[75%] px-4 py-3 rounded-2xl shadow-sm ${
          isUser
            ? "bg-blue-600 text-white"
            : "bg-gray-100 text-gray-900"
        }`}
      >
        <strong className="block text-sm mb-1">
          {isUser ? "👤 You" : "🤖 Assistant"}
        </strong>

        <p className="break-words">{message}</p>
      </div>
    </div>
  );
}

export default ChatMessage;