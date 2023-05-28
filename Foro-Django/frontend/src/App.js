// Importamos react para poder usarlo
import React from 'react';

// Importamos los componentes que creamos
import Landing from './components/Landing';
import Header from './components/Header';



function App() {
  return (
    <>
      <Header />
      <Landing />
    </>
  );
}


// Exportamos por defecto el componente
export default App;