import React from 'react';
import { Footer } from '../components/Footer/Footer';
import { Header } from '../components/Header/Header';
import { Building } from '../models';
import { buildingsdata } from '../data/Buildingsdata';
import { BuildingObject } from '../components/Building/Building';


export function BuildingsPage () {

 
  return (
    <div>
      <Header/>
      <p>Объекты управляющей компании</p>
      <div className='container-buildings-page'>
        {buildingsdata.map((building_ob: Building) => <BuildingObject building_ob={building_ob} key={building_ob.number}/>)}
      </div>
      <Footer/>

    </div>
  )
}
