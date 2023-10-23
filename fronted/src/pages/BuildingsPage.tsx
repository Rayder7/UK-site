import React from 'react';
import { Footer } from '../components/Footer/Footer';
import { Header } from '../components/Header/Header';
import { Building } from '../models';
import { buildingsdata } from '../data/Buildingsdata';
import { BuildingObject } from '../components/Building/Building';
import '../index.css'

export function BuildingsPage () {

 
  return (
    <div>
      <Header/>
      <div className='container-buildings-page'>
        <h1>Объекты управляющей компании</h1>
        {buildingsdata.map((building_ob: Building) => <BuildingObject building_ob={building_ob} key={building_ob.number}/>)}
      </div>
      <Footer/>

    </div>
  )
}
