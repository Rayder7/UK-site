import React from  "react"
import './Building.css'
import { Building } from "../../models"
import { NavLink } from "react-router-dom";
import Newobject  from  "../../static/img/newsobject.jpg"
import { BuildingButton } from "../UI/Button/BuildingButton";
import { BsFillBuildingFill} from "react-icons/bs";
import { HiSquares2X2 } from "react-icons/hi2";

interface BuildingProps {
    building_ob: Building
}

export function BuildingObject({building_ob}: BuildingProps) {
    return (
        <div className="container-building-object">
          <div className="container-building-img">
            <img src={Newobject} alt="dom"/>
          </div>
          <div className='containter-building-info'>
            <div className='building-info-column'>
              <BsFillBuildingFill/>
              ул. {building_ob.street}, дом {building_ob.number}
            </div>
            <div className='building-info-column'>
              <HiSquares2X2/>
              {building_ob.square}
            </div>
          </div>
          <NavLink to='/' className='nav-link'>
            <BuildingButton/>
          </NavLink>
        </div>
    )
}