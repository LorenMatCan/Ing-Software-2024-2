import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import { Button } from 'react-bootstrap';
import { useState } from 'react';
import { NuevaRenta } from './rentas/NuevaRenta.js';
import { ActualizarRentas } from './rentas/ActualizarRenta.js';
import { VerRentas } from './rentas/VerRentas.js';
import { BorrarRenta } from './rentas/BorrarRenta.js'
import "./Rentas.css";



export const RentasIndice = () => {
    const [Contenido, setContenido] = useState(0);
    const [Rentas, setRentas] = useState([
        {id:1, idUsuario:1, idPelicula:1, fechaRenta:"2021-10-10", dias:5, estado:0},
        {id:2, idUsuario:2, idPelicula:2, fechaRenta:"2021-10-10", dias:5, estado:1},
        {id:3, idUsuario:3, idPelicula:3, fechaRenta:"2021-10-10", dias:5, estado:1}
    ]);

    function ActualizarListaRentas(nuevaLista){
        setRentas(nuevaLista);
    }

    return (

        <div className="Contenedor">
            <h1>Rentas</h1>
            <Row>
                <Col>
                    <Button variant="outline-light"onClick={() => setContenido(1)}>Registrar Renta</Button>
                </Col>
                <Col>
                    <Button variant="outline-light" onClick={() => setContenido(2)}>Actualizar Renta</Button>
                </Col>
                <Col>
                    <Button variant="outline-light"onClick={() => setContenido(3)}>Ver Renta</Button>
                </Col>
                <Col>
                    <Button variant="outline-light" onClick={() => setContenido(4)}>Eliminar Renta</Button>
                </Col>
            </Row>
        
            <div className="Cuerpo">
                {Contenido === 1 && <NuevaRenta rentas={Rentas} funcion={ActualizarListaRentas}/>}
                {Contenido === 3 && <VerRentas rentas={Rentas} />}
                {Contenido === 2 && <ActualizarRentas rentas={Rentas} funcion={ActualizarListaRentas}/>}
                {Contenido === 4 && <BorrarRenta rentas={Rentas} funcion={ActualizarListaRentas}/>}
               
            </div>  
        </div>


    );
 } 

