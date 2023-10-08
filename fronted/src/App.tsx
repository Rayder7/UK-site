import React from 'react';
import {Route, Routes} from 'react-router-dom';
import { NewsPage } from './pages/NewsPage';
import { AboutPage } from './pages/About';


function App() {
  return (
    <Routes>
      <Route path="/news" element={ <NewsPage />} ></Route>
      <Route path="/about" element={ <AboutPage />} ></Route>
    </Routes>
  )
}

export default App;
