import React from 'react';

import { New } from '../models';
import { NewObject } from '../components/News/New';
import { newsdata } from "../data/Newsdata"
import { Header } from '../components/Header/Header';
import { Footer } from '../components/Footer/Footer';
import '../index.css'

export function NewsPage () {

 
  return (
    <div>
      <Header/>
      <div className='container-news-page'>
      <h2>Новости</h2> 
        {newsdata.map((news: New) => <NewObject news={news} key={news.title}/>)}
      </div>
      <Footer/>
    </div>
  )
}
