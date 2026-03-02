import { createBrowserRouter, createHashRouter } from 'react-router-dom';
import App from './App';
import HomePage from "./pages/HomePage";
import NotFoundPage from './pages/NotFoundPage';
import AboutPage from './pages/AboutPage'
import CharacterPage from './pages/CharacterPage'

const PROD = JSON.parse(import.meta.env.VITE_PROD)

const createRouter = PROD ? createHashRouter : createBrowserRouter

const router = createRouter([{
    path: '/',
    element:<App/>,
    errorElement: <NotFoundPage/>,
    children: [{
        index: true,
        element: <HomePage/>
    }, {
        path:'about',
        element: <AboutPage/>
    }, {
        path:'character-cards',
        element: <CharacterPage/>
    }, {
        path:'*',
        element: <NotFoundPage/>
    }]
}]);

export default router;