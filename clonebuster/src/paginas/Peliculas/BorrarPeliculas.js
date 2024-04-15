import { Row } from "react-bootstrap";
import { Col } from "react-bootstrap";
import { Button } from "react-bootstrap";
import { Container } from "react-bootstrap";  
import { useState } from "react";  


export function BorrarUsuarios({usuarios,funcion}) {
    const [idN, setId] = useState(0);

    const handleId = (event) => {
        setId(event.target.value);
    } 

    function borrarUsuario(){
        const id = parseInt(idN);
        const nuevaLista = usuarios.filter((usr) => usr.id !== id);
        funcion(nuevaLista); 
    }

    function borrarTodos(){
        funcion([]);
    }

    return (
        <div>   
        <h3>BorrarUsuario</h3>
        <Container>
            <Row>
                <Col>
                <label>id:</label>
                <input type="number" onChange={handleId}/>
                <Button variant="outline-light" onClick={borrarUsuario}>BorrarUsuario</Button>
                </Col>
            </Row>            
        </Container>
        
        <Container>
            <h3 >Borrar todos los usuarios</h3>
            <Button variant="outline-light" onClick={borrarTodos}>Borrar todos los usuarios</Button>
         
        </Container>
        </div>
    );
}