function Sidebar({
    sessions,
    selectedSession,
    onSelectSession,
    onNewChat,
    onClose
}) {

    return (

        <div className="sidebar">

            <div className="sidebar-header">

                <h2> Chat History</h2>

                <button
                    onClick={onClose}
                    className="close-btn">

                        ✕
                </button>
            </div>

            <button 
                className="new-chat-btn"
                onClick={onNewChat}>

                    + New Chat
                </button>

            <div className="history-list">

                {sessions.length === 0 ? (

                    <p>No previous chats</p>

                ) : (

                sessions.map((session) => (

                    <div
                        key={session.session_id}
                        className={
                            selectedSession === session.session_id
                                ? "history-item active"
                                : "history-item"
                        }
                        onClick={() =>
                            onSelectSession(session.session_id)
                        }
                    >
                        {session.title}
                    </div>

                ))

                )}

            </div>

        </div>

    );
}

export default Sidebar;