import { FaFileAlt, FaRobot, FaSearch } from "react-icons/fa";

function Features() {
  return (
    <section className="py-20 bg-gray-50">
      <div className="max-w-7xl mx-auto px-6">

        <h2 className="text-4xl font-bold text-center mb-12">
          Why Use Our AI Assistant?
        </h2>

        <div className="grid md:grid-cols-3 gap-8">

          {/* Card 1 */}
          <div className="bg-white p-8 rounded-xl shadow-lg hover:shadow-xl transition">
            <FaFileAlt className="text-5xl text-blue-600 mb-4" />
            <h3 className="text-2xl font-semibold mb-3">
              Document Search
            </h3>
            <p className="text-gray-600">
              Search across company policies, employee handbooks, and internal documents instantly.
            </p>
          </div>

          {/* Card 3 */}
          <div className="bg-white p-8 rounded-xl shadow-lg hover:shadow-xl transition">
            <FaRobot className="text-5xl text-purple-600 mb-4" />
            <h3 className="text-2xl font-semibold mb-3">
              AI Assistant
            </h3>
            <p className="text-gray-600">
              Chat naturally with an AI assistant that remembers your conversation history.
            </p>
          </div>

        </div>

      </div>
    </section>
  );
}

export default Features;