// Importamos createStore, combineReducers, applyMiddleware para la creación del store (almacén de datos)
import { createStore, combineReducers, applyMiddleware } from 'redux';

// Importamos thunk para poder hacer peticiones asíncronas
import thunk from 'redux-thunk';

// Importamos composeWithDevTools para poder usar la extensión de Redux DevTools
import { composeWithDevTools } from 'redux-devtools-extension';

// Importamos los reducers que creamos
import { userLoginReducer } from './reducers/userReducer';




// Creamos el reducer para el login
const reducer = combineReducers({
    userLogin: userLoginReducer,
});



// Obtenemos el usuario de la sesión
const userInfoStorage = localStorage.getItem('userInfo') ? JSON.parse(localStorage.getItem('userInfo')) : null;



// Creamos el estado inicial
const initialState = {
    userLogin: { userInfo: userInfoStorage },
};



// Creamos la constante de midelware para poder hacer peticiones asíncronas
const middleware = [thunk];




// Creamos la constante de store
const store = createStore( reducer, initialState, composeWithDevTools( applyMiddleware(...middleware) ) );


// Exportamos el store
export default store;