import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import { Button } from 'react-bootstrap';
import { useState } from 'react';
import { NuevaPelicula, NuevoUsuario } from './peliculas/NuevaPelicula.js';
import { ActualizarPeliculas } from './peliculas/ActualizarPeliculas.js';
import { VerPeliculas } from './peliculas/VerPeliculas.js';
import { BorrarPeliculas } from './peliculas/BorrarPeliculas.js'
import "./Usuarios.css";



export const PeliculasIndice = () => {
    const [Contenido, setContenido] = useState(0);
    const [Peliculas, setPeliculas] = useState([
        {id: 1, nombre: "Nimona", genero: "Aventura",duracion:"140", inventario:"10"},
        {id: 2, nombre: "El señor de los anillos", genero: "Aventura",duracion:"180", inventario:"10"},
        {id: 3, nombre: "Star Wars 29", genero: "Aventura",duracion:"120", inventario:"10"}
    ]);

    function ActualizarListaPeliculas(nuevaLista){
        setPeliculas(nuevaLista);
    }

    return (

        <div className="Contenedor">
            <h1>Peliculas</h1>
            <Row>
                <Col>
                    <Button variant="outline-light"onClick={() => setContenido(1)}>Ingresar Pelicula</Button>
                </Col>
                <Col>
                    <Button variant="outline-light" onClick={() => setContenido(2)}>Actualizar Pelicula</Button>
                </Col>
                <Col>
                    <Button variant="outline-light"onClick={() => setContenido(3)}>Ver Peliculas</Button>
                </Col>
                <Col>
                    <Button variant="outline-light" onClick={() => setContenido(4)}>Eliminar Pelicula</Button>
                </Col>
            </Row>
        
            <div className="Cuerpo">
                {Contenido === 1 && <NuevaPelicula peliculas={Peliculas} funcion={ActualizarListaPeliculas} />}
                {Contenido === 2 && <ActualizarPeliculas peliculas={Peliculas} funcion={ActualizarListaPeliculas} />}
                {Contenido === 3 && <VerPeliculas peliculas={Peliculas} />}
                {Contenido === 4 && <BorrarPeliculas peliculas={Peliculas} funcion={ActualizarListaPeliculas} />}

            </div>  
        </div>


    );
 } 

