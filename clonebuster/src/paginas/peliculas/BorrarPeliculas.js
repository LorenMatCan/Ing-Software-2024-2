import { Row } from "react-bootstrap";
import { Col } from "react-bootstrap";
import { Button } from "react-bootstrap";
import { Container } from "react-bootstrap";  
import { useState } from "react";  


export function BorrarPeliculas({peliculas,funcion}) {
    const [idN, setId] = useState(0);

    const handleId = (event) => {
        setId(event.target.value);
    } 

    function borrarPelicula(){
        const id = parseInt(idN);
        const nuevaLista = peliculas.filter((peli) => peli.id !== id);
        funcion(nuevaLista); 
    }

    function borrarTodos(){
        funcion([]);
    }

    return (
        <div>   
        <h3>Borrar Peliculas de inventario</h3>
        <Container>
            <Row>
                <Col>
                <label>id:</label>
                <input type="number" onChange={handleId}/>
                <Button variant="outline-light" onClick={borrarPelicula}>Borrar Pelicula</Button>
                </Col>
            </Row>            
        </Container>
        
        <Container>
            <h3 >Borrar inventario</h3>
            <Button variant="outline-light" onClick={borrarTodos}>Borrar inventario</Button>
         
        </Container>
        </div>
    );
}