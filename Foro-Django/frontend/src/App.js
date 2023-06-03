// Importamos react para poder usarlo
import React from "react";

// Importamos BrowserRouter, Route y Routes para las rutas de la aplicación
import { BrowserRouter, Route, Routes } from "react-router-dom";

// Importamos los componentes que creamos
import Landing from "./components/Landing";
import Header from "./components/Header";
import Login from "./components/Login";
import Register from "./components/Register";
import PrivateRoute from "./components/PrivateRoute";

function App() {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route element={<PrivateRoute />}></Route>
        <Route path="/landing" element={<Landing />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
      </Routes>
    </BrowserRouter>
  );
}

// Exportamos por defecto el componente
export default App;