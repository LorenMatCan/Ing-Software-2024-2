import { Container } from "react-bootstrap"
import { Row } from "react-bootstrap"
import { Col } from "react-bootstrap"
import { Button } from "react-bootstrap"
import { useState } from "react"


export function ActualizarPeliculas({peliculas,funcion}) {
    const [PeliculaSelecionado, setPeliculaSe] = useState(undefined);
    const [pelicula, setPelicula] = useState(false);
    const [peliculaEditar, setPeliculaEditar] = useState("");   
    const [id, setId] = useState(0);

    const handleId = (event) => {
        setId(event.target.value);
    }
    
    const buscarPelicula = () => {
        const idN = parseInt(id);
        const peliculaEditar = peliculas.find((peli) => peli.id === idN);
        setPeliculaEditar(peliculaEditar);
        if (peliculaEditar!==undefined){
            setPeliculaEditar("");
            setPelicula(true)
            setPeliculaSe(peliculaEditar);
        }
        else{
            setPelicula(false)
        }
    }




    return (
        <div>   
        <h3>Actualizar Pelicula</h3>
        <Container>
            <Row>
                <Col>
                <label>id:</label>
                <input type="number" onChange={handleId}/>
                <Button variant="outline-light" onClick={buscarPelicula}>Buscar</Button>
                </Col>
            </Row>
            {pelicula ? <ActualizarPelicula id = {id} funcion={funcion} peliculas={peliculas} peliculaAE={PeliculaSelecionado} estado={setPelicula}/> : "No se encontro la pelicula"}
            
        </Container>
        </div>
    )

    
}


function ActualizarPelicula ({id,funcion,peliculas, peliculaAE,estado})  { 
    const [nombre, setNombre] = useState("");
    const [genero, setGenero] = useState("");
    const [duracion, setDuracion] = useState("");
    const [inventario, setInventrio] = useState("");

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


    function actualizarLista( ) {
        const idN = parseInt(id);
        const peliculaNueva ={nombre:nombre, genero:genero, duracion:duracion, inventario:inventario};

        const nuevaLista = peliculas.map((peli) => {
            if (peli.id === idN){
                return peliculaNueva;
            }
            return peli;
        });
        funcion(nuevaLista);
        estado(false)

    }

    return (
        <div>
            <h3>Solo modifique los campos que desee editar, evite de tocar todos aquellos que esten correctos.</h3>
             <Container>
        <Row >
            <Col>
                <label>Nombre:</label>
            </Col>
            <Col>
                <input type="text" required onChange={handleNombre} defaultValue={peliculaAE.nombre}/>
            </Col>
            <Col>
                <label>Genero:</label>
            </Col>
            <Col>
                <input type="text" required onChange={handleGenero} defaultValue={peliculaAE.genero}/>
            </Col>
            <Col>
                <label>Duración(en minutos):</label>
            </Col>
            <Col>
                <input type="number" required onChange={handleDuracion} defaultValue={peliculaAE.duracion}/>
            </Col>
        </Row> 
        <Row>
            <Col>Inventario: <input type="number" required onChange={handleInventario} defaultValue={peliculaAE.inventario}></input></Col>
        
        </Row>
            <Button variant="outline-light" type="submit" onClick={actualizarLista}>Guardar</Button>
        </Container>

            
       
    </div>
    )
}

