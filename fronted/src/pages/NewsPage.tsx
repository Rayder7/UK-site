import React from 'react';

import { New } from '../models';
import { NewObject } from '../components/News/New';
import { newsdata } from "../data/Newsdata"
import { Header } from '../components/Header/Header';
import { Footer } from '../components/Footer/Footer';

export function NewsPage () {

 
  return (
    <div>
      <Header/>
      <div className='container-news-page'>
      <p>Новости</p> 
        {newsdata.map((news: New) => <NewObject news={news} key={news.title}/>)}
        
      </div>
      <Footer/>
    </div>
  )
}
