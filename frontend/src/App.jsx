import { useState , useEffect} from "react";
// import Sidebar from "./components/Sidebar";
// import ChatBot from "./components/ChatBot";
import Header from "./components/Header";
import Hero from "./components/Hero";
import Features from "./components/Features";
import Footer from "./components/Footer";
import ChatWidget from "./components/ChatWidget"
import EmployeeManagement from "./pages/EmployeeManagement";

import "./App.css";

function App() {


   const [selectedSession, setSelectedSession] = useState(() => {
    return(
      localStorage.getItem("session_id") ||
      crypto.randomUUID()
    );
  });

  
  const [sessions, setSessions] = useState([]);

  const loadSessions = async () => {

    const response = await fetch(
      "http://127.0.0.1:8000/sessions"
    );

    const data = await response.json();
    setSessions(data.sessions);
  };

  const handleSelectSession = (sessionId) => {

    localStorage.setItem(
      "session_id",
      sessionId
    );
     setSelectedSession(sessionId);
  }


   useEffect(() => {
    loadSessions();
  }, []);

  const handleNewChat = () => {
    const newSession = crypto.randomUUID();
    localStorage.setItem("session_id", newSession);
    setSelectedSession(newSession)
  }
  
  return(
    

     <div className="min-h-screen bg-gray-100">
      <Header/>

      <Hero/>

      <Features/>

      <EmployeeManagement/>

      <Footer/>

      <ChatWidget
         sessionId={selectedSession}
         selectedSession={selectedSession}
         sessions={sessions}
         refreshSessions={loadSessions}
         onNewChat={handleNewChat} 
         onSelectSession={handleSelectSession}
        />

      {/* <Sidebar 
        sessions={sessions}
        selectedSession={selectedSession}
        onSelectSession={setSelectedSession}
        onNewChat={handleNewChat}
      /> */}

      {/* <ChatBot 
        sessionId={selectedSession}
        refreshSessions={loadSessions}
      /> */}

    </div>
  );
}

export default App;

// TO CHECK WHETHER TAILWIND IS WORKING OR NOT

// function App() {
//   return (
//     <div className="min-h-screen bg-blue-600 flex items-center justify-center">
//       <h1 className="text-5xl font-bold text-white">
//         Tailwind is Working 🚀
//       </h1>
//     </div>
//   );
// }

// export default App;