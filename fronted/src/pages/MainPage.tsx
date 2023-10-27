import React from 'react';
import { Footer } from '../components/Footer/Footer';
import { Header } from '../components/Header/Header';
import '../index.css'
import { MainInfo } from '../components/MainInfo/MainInfo';

export function MainPage () {

 
  return (
    <div className='container-main-page'>
      <Header/>
      <MainInfo/>
      <Footer/>
    </div>
  )
}
