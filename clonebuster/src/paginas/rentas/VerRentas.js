import Table from 'react-bootstrap/Table';
import { useState } from 'react';


export const VerRentas = ({rentas}) => {
  function vencido (renta){
    var fecha = new Date(renta.fechaRenta);
    var hoy = new Date();
    var dias = renta.dias;
    fecha.setDate(fecha.getDate() + dias);
    if (fecha < hoy && renta.estado === 0){
      return 'table-warning';
    }
    else{
      return 'black';
    }
  }



    return (
        <div>
        <h1>Lista de Usuarios</h1>

<Table striped bordered hover size="sm" variant="dark">
      <thead>
        <tr>
          <th>id</th>
          <th>idUsuario</th>
          <th>idPelicula</th>
          <th>Fecha Renta</th>
          <th>Días renta</th>
          <th>Estado</th>
        </tr>
      </thead>
      <tbody>
      {rentas.map((ren, key)=>{
                    return(
                        <tr key={key}  class={vencido(ren)}>
                            <td>{ren.id}</td>
                            <td>{ren.idUsuario}</td>
                            <td>{ren.idPelicula}</td>
                            <td>{ren.fechaRenta}</td>
                            <td>{ren.dias}</td>
                            <td>{ren.estado}</td>
                        </tr>
                    );
                })}
      </tbody>
    </Table>


        </div>
    );
}