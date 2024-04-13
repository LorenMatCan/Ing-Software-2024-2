import './App.css';
import { BrowserRouter as Router, Routes,Route,Link} from 'react-router-dom';
import { Indice } from './paginas/Indice';
import { UsuariosIndice } from './paginas/Usuarios';
import { PeliculasIndice } from './paginas/Peliculas';
import { RentasIndice } from './paginas/Rentas';
import { Container}  from 'react-bootstrap';
import { Nav } from 'react-bootstrap';
import { Navbar } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <div className="App">
      <Router>
        <Navbar bg="dark" data-bs-theme="dark">
          <Container>
            <Nav className="me-auto">
              <Nav.Link href="/">Inicio</Nav.Link>
              <Nav.Link href="/usuarios">Usuarios</Nav.Link>
              <Nav.Link href="/peliculas">Peliculas</Nav.Link>
              <Nav.Link href="/rentas">Rentas</Nav.Link>
            </Nav>
          </Container>
        </Navbar>
        
        <Routes>
          <Route path= "/" element={<Indice />} />
          <Route path="/usuarios" element={<UsuariosIndice />} />
          <Route path="/peliculas" element={<PeliculasIndice />} />
          <Route path="/rentas" element={<RentasIndice />} />
          <Route path="*" element={<h1>404 Not Found</h1>} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
