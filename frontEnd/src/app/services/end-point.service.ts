import { Injectable } from '@angular/core';

@Injectable()

export class EndPointService {
  isDev : boolean;
  constructor() {
    this.isDev = false; // change in real test
  }
  prepEndPoint( ep ){
    if( this.isDev ) {
      return ep;
    } else{
      return 'http://localhost:8000/'+ep;
    }
  }
}
