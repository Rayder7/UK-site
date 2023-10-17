import React from 'react';
import {Route, Routes} from 'react-router-dom';
import { NewsPage } from './pages/NewsPage';
import { AboutPage } from './pages/AboutPage';
import { MainPage } from './pages/MainPage';
import { ContactsPage } from './pages/ContactsPage';
import { BuildingsPage } from './pages/BuildingsPage';
import { ServicePage } from './pages/ServicePage';


function App() {
  return (
    <Routes>
      <Route path="/" element={ <MainPage />} ></Route>
      <Route path="/about" element={ <AboutPage />} ></Route>
      <Route path="/contacts" element={ <ContactsPage />} ></Route>
      <Route path="/news" element={ <NewsPage />} ></Route>
      <Route path="/buildings" element={ <BuildingsPage />} ></Route>
      <Route path="/service" element={ <ServicePage />} ></Route>
    </Routes>
  )
}

export default App;
