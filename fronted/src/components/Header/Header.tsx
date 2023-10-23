import React from 'react'
import './Header.css'
import { NavLink } from "react-router-dom";
import logo  from  "../../static/img/logoMain.png"


export function Header() {
  return (
    <div className='header'>
      <div className='logocompany'>
        <NavLink to='/' className='nav-link'>
          <div className='logo-header'>
            <img src={logo} width="50" height="50"/>
          </div>
        </NavLink>
      </div>
      <div className='navigation'>
        <NavLink to='/about' className='nav-link'>Компания</NavLink>
        <NavLink to='/buildings' className='nav-link'>Объекты</NavLink>
        <NavLink to='/service' className='nav-link'>Услуги</NavLink>
        <NavLink to='/news' className='nav-link'>Новости</NavLink>
        <NavLink to='/contacts' className='nav-link'>Контакты</NavLink>
      </div>
    </div>
  )
}