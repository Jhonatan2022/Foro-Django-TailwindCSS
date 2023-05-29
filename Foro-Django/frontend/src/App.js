// Importamos react para poder usarlo
import React from "react";

// Importamos BrowserRouter, Route y Routes para las rutas de la aplicación
import { BrowserRouter, Route, Routes } from "react-router-dom";

// Importamos los componentes que creamos
import Landing from "./components/Landing";
import Header from "./components/Header";
import Login from "./components/Login";



function App() {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/landing" element={<Landing />} />
        <Route path="/login" element={<Login />} />
      </Routes>
    </BrowserRouter>
  );
}


// Exportamos por defecto el componente
export default App;