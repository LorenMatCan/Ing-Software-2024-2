import { Col, Container } from "react-bootstrap";
import { Row } from "react-bootstrap";
import { Button } from "react-bootstrap";
import { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";

export function NuevaPelicula ({peliculas, funcion})  {
    const [nombre, setNombre] = useState("");
    const [genero, setGenero] = useState("");
    const [duracion, setDuracion] = useState("");
    const [inventario, setInventrio] = useState("");
    const [id, setId] = useState(peliculas.length + 1);

    const handleNombre = (event) => {
        setNombre(event.target.value);
    } 

    const handleGenero = (event) => {
        setGenero(event.target.value);
    }

    const handleDuracion = (event) => {
        setDuracion(event.target.value);
    }

    const handleInventario = (event) => {
        setInventrio(event.target.value);
    }


    const anadirPelicula = () => {
        setId(id + 1);
        const nuevaPelicula ={id:id, nombre:nombre, genero:genero, duracion:duracion, inventario:inventario};
        const nuevaLista = [...peliculas, nuevaPelicula];
        funcion(nuevaLista);
    }
    
    return (
        <div>
            
            <h3>Añadir película a inventario</h3>
            <Container>
            <Row >
                <Col>
                    <label>Nombre:</label>
                </Col>
                <Col>
                    <input type="text" required onChange={handleNombre}/>
                </Col>
                <Col>
                    <label>Genero:</label>
                </Col>
                <Col>
                    <input type="text" required onChange={handleGenero}/>
                </Col>
                <Col>
                    <label>Duracion(en minutos):</label>
                </Col>
                <Col>
                    <input type="number" required onChange={handleDuracion}/>
                </Col>
            </Row> 
            <Row>
                <Col>Inventario: <input type="number" required onChange={handleInventario}></input></Col>
            </Row>
                <Button variant="outline-light" type="submit" onClick={anadirPelicula}>Guardar</Button>
            </Container>

        </div>
    

    );
}



