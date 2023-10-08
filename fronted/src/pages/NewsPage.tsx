import React from 'react';

import { New } from '../models';
import { NewsList } from '../components/News/News';
import { newsdata } from "../data/Newsdata"

export function NewsPage () {

 
  return (
    <div className='container mx-auto max-w-3xl pt-4'>

      {newsdata.map((news: New) => <NewsList news={news} key={news.title} />) }
      
    </div>
  )
}
