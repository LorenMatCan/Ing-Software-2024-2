import Table from 'react-bootstrap/Table';


export const VerPeliculas = ({peliculas}) => {
    return (
        <div>
        <h1>Inventario</h1>



<Table striped bordered hover size="sm" variant="dark">
      <thead>
        <tr>
          <th>id</th>
          <th>Nombre</th>
          <th>Genero</th>
          <th>duracion</th>
          <th>Inventario</th>
        </tr>
      </thead>
      <tbody>
      {peliculas.map((peli, key)=>{
                    return(
                        <tr key={key}>
                            <td>{peli.id}</td>
                            <td>{peli.nombre}</td>
                            <td>{peli.genero}</td>
                            <td>{peli.duracion}</td>
                            <td>{peli.inventario}</td>
                        </tr>
                    );
                })}
      </tbody>
    </Table>


        </div>
    );
}