function Header() {
  return (
    <header className="bg-white shadow-md">
      <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">

        {/* Logo */}
        <div className="flex items-center gap-2">
          <span className="text-3xl">🤖</span>
          <h1 className="text-2xl font-bold text-blue-600">
            ABC Technologies
          </h1>
        </div>

        {/* Navigation */}
        <nav className="flex gap-8 text-gray-700 font-medium">
          <a href="#" className="hover:text-blue-600">Home</a>
          <a href="#" className="hover:text-blue-600">About</a>
          <a href="#" className="hover:text-blue-600">Services</a>
          <a href="#" className="hover:text-blue-600">Contact</a>
        </nav>

      </div>
    </header>
  );
}

export default Header;