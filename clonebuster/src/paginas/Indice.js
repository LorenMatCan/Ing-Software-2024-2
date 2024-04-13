import './Indice.css';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Image from 'react-bootstrap/Image';
import { Link } from 'react-router-dom';
 
 
 export const Indice = () => {
    return (
        <div className="Contenedor">
            <h1>CloneBuster</h1>
            <h2>El mejor servicio de renta de peliculas</h2>
            <Container>
                <Row>
                    <Col >
                     <Row>
                        <Col>Usuarios</Col>
                     </Row>
                     <Row>
                        <Col><Image src={require('./imagenes/usuario.png')} width="30%" id='Imagen' /></Col>
                     </Row>
                    </Col>
                    <Col >
                    <Row>
                        <Col>Películas</Col>
                    </Row>
                     <Row>
                        <Col ><Image src={require('./imagenes/peliculas.png')} width="40%"/></Col>
                     </Row>
                    </Col>
                    <Col xs={6} md={4} >Rentas</Col>
                </Row>
            </Container>
        </div>
    )
 } 