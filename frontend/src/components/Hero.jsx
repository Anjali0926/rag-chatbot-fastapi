function Hero() {
  return (
    <section className="bg-gradient-to-r from-blue-600 to-indigo-700 text-white py-24">
      <div className="max-w-7xl mx-auto px-6 text-center">

        <h1 className="text-5xl font-bold mb-6">
          AI-Powered Company Knowledge Assistant
        </h1>

        <p className="text-xl max-w-3xl mx-auto mb-10">
          Get instant answers from company documents using our AI-powered
          Retrieval-Augmented Generation (RAG) chatbot.
        </p>

        <div className="flex justify-center gap-4">
          <button className="bg-white text-blue-600 font-semibold px-6 py-3 rounded-lg hover:bg-gray-100 transition">
            Start Chat
          </button>

          <button className="border border-white px-6 py-3 rounded-lg hover:bg-white hover:text-blue-600 transition">
            Learn More
          </button>
        </div>

      </div>
    </section>
  );
}

export default Hero;