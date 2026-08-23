import { FaGithub, FaLinkedin, FaEnvelope } from "react-icons/fa";

function Footer() {
  return (
    <footer className="bg-gray-900 text-white py-10">

      <div className="max-w-7xl mx-auto px-6">

        <div className="grid md:grid-cols-3 gap-8">

          {/* Company */}
          <div>
            <h2 className="text-2xl font-bold text-blue-400">
              ABC Technologies
            </h2>

            <p className="mt-3 text-gray-300">
              AI-powered document assistant built using
              React, FastAPI, PostgreSQL, LangChain,
              LangGraph and RAG.
            </p>
          </div>

          {/* Quick Links */}
          <div>
            <h3 className="text-xl font-semibold mb-3">
              Quick Links
            </h3>

            <ul className="space-y-2 text-gray-300">
              <li className="hover:text-white cursor-pointer">
                Home
              </li>

              <li className="hover:text-white cursor-pointer">
                About
              </li>

              <li className="hover:text-white cursor-pointer">
                Services
              </li>

              <li className="hover:text-white cursor-pointer">
                Contact
              </li>
            </ul>
          </div>

          {/* Contact */}
          <div>
            <h3 className="text-xl font-semibold mb-3">
              Contact
            </h3>

            <div className="space-y-3">

              <div className="flex items-center gap-2">
                <FaEnvelope />
                <span>support@abctech.com</span>
              </div>

              <div className="flex items-center gap-2">
                <FaGithub />
                <span>GitHub</span>
              </div>

              <div className="flex items-center gap-2">
                <FaLinkedin />
                <span>LinkedIn</span>
              </div>

            </div>
          </div>

        </div>

        <hr className="my-8 border-gray-700" />

        <p className="text-center text-gray-400">
          © 2026 ABC Technologies. All Rights Reserved.
        </p>

      </div>

    </footer>
  );
}

export default Footer;