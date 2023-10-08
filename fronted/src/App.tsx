import React from 'react';
import {Route, Routes} from 'react-router-dom';
import { NewsPage } from './pages/NewsPage';


function App() {
  return (
    <Routes>
      <Route path="/" element={ <NewsPage />} ></Route>
    </Routes>
  )
}

export default App;
