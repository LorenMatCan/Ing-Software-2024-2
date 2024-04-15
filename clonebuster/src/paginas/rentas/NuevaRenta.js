import { Col, Container } from "react-bootstrap";
import { Row } from "react-bootstrap";
import { Button } from "react-bootstrap";
import { useState } from "react";

import "bootstrap/dist/css/bootstrap.min.css";

export function NuevaRenta({rentas, funcion})  {
    const [id, setId] = useState(rentas.length + 1);
    const [idUsuario, setIdUsuario] = useState(0);
    const [idPelicula, setIdPelicula] = useState(0);
    const [dias, setDias] = useState(5);

    const handleIdUsuario = (event) => {
        setIdUsuario(event.target.value);
    }
    const handleIdPelicula = (event) => {
        setIdPelicula(event.target.value);
    }

    const handleDias = (event) => {
        setDias(event.target.value);
    }


    const addRenta = () => {
        setId(id + 1);
        const hoy = new Date();
        const fechaRenta = hoy.getFullYear() + "-" + (hoy.getMonth() + 1) + "-" + hoy.getDate();
        const nuevaRenta = {id: id, idUsuario: idUsuario, idPelicula: idPelicula, fechaRenta: fechaRenta, dias: dias, estado: 0};
        const nuevaLista = [...rentas, nuevaRenta];
        funcion(nuevaLista);
    }
    
    return (
        <div>
            
            <h3> Ingrese una nueva renta</h3>
            <Container>
            <Row >
                <Col>
                    <label>idUsuario:</label>
                </Col>
                <Col>
                    <input type="number" required onChange={handleIdUsuario}/>
                </Col>
                <Col>
                    <label>idPelicula:</label>
                </Col>
                <Col>
                    <input type="number" required onChange={handleIdPelicula}/>
                </Col>
            </Row> 
            <Row>
                <Col>dias de renta: <input type="number" required onChange={handleDias}></input></Col>
                
            </Row>
                <Button variant="outline-light" type="submit" onClick={addRenta}>Guardar</Button>
            </Container>

        </div>
    

    );
}



