// import { useState } from "react";
// import reactLogo from "./assets/react.svg";
// import viteLogo from "/vite.svg";

import { Chip } from "./components/chip";

function App() {
  return (
    <div className="min-h-screen bg-secondary text-primary flex items-center justify-center">
      <div className="w-full max-w-sm p-24">
        <Chip label="3명" />
      </div>
    </div>
  );
}

export default App;
