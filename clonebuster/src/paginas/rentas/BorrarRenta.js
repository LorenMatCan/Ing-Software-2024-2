import { Row } from "react-bootstrap";
import { Col } from "react-bootstrap";
import { Button } from "react-bootstrap";
import { Container } from "react-bootstrap";  
import { useState } from "react";  


export function BorrarRenta({rentas,funcion}) {
    const [idN, setId] = useState(0);

    const handleId = (event) => {
        setId(event.target.value);
    } 

    function borrarRenta(){
        const id = parseInt(idN);
        const nuevaLista = rentas.filter((ren) => ren.id !== id);
        funcion(nuevaLista); 
    }

    function borrarTodos(){
        funcion([]);
    }

    return (
        <div>   
        <h3>Borrar Renta</h3>
        <Container>
            <Row>
                <Col>
                <label>id:</label>
                <input type="number" onChange={handleId}/>
                <Button variant="outline-light" onClick={borrarRenta}>Borrar Renta</Button>
                </Col>
            </Row>            
        </Container>
        
        <Container>
            <h3 >Borrar todos las rentas</h3>
            <Button variant="outline-light" onClick={borrarTodos}>Borrar todos las rentas</Button>
         
        </Container>
        </div>
    );
}