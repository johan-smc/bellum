import { Injectable } from '@angular/core';
import {Http, Headers} from "@angular/http";
import {EndPointService} from './end-point.service';
import {AuthService} from './auth.service';

@Injectable({
  providedIn: 'root'
})
export class FileService {

  constructor(
    private http : Http,
    private endPoint : EndPointService,
    private authService : AuthService
  ) { }

  getFiles(father)
  {
    let headers = new Headers();
    headers.append('Content-Type','application/json');
    headers.append('Authorization','Token '+this.authService.getToken());
    let ep = this.endPoint.prepEndPoint('get_inodes/');
    return this.http.post(ep, father,{headers:headers})
  }
  getAllFiles()
  {
    let headers = new Headers();
    headers.append('Content-Type','application/json');
    headers.append('Authorization','Token '+this.authService.getToken());
    let ep = this.endPoint.prepEndPoint('get_inodes/');
    return this.http.get(ep,{headers:headers})
  }

  getFile(file)
  {
    let headers = new Headers();
    headers.append('Content-Type','application/json');
    headers.append('Authorization','Token '+this.authService.getToken());
    let ep = this.endPoint.prepEndPoint('get_file/');
    return this.http.post(ep, file,{headers:headers})
  }
  postFile(fileToUpload,name,idFather) {

    let headers = new Headers();
    headers.append('Authorization','Token '+this.authService.getToken());
    let ep = this.endPoint.prepEndPoint('upload_file/');
    var formData = new FormData();
    formData.append("name", name);
    formData.append("file",  fileToUpload);
    if( idFather)
      formData.append("father",  idFather);
    return this.http
      .post(ep, formData, { headers: headers })
  }
  createFolder(folder)
  {
    let headers = new Headers();
    headers.append('Content-Type','application/json');
    headers.append('Authorization','Token '+this.authService.getToken());
    let ep = this.endPoint.prepEndPoint('create_folder/');
    return this.http.post(ep, folder,{headers:headers})
  }

  getFilesGroup(father)
  {
    let headers = new Headers();
    headers.append('Content-Type','application/json');
    headers.append('Authorization','Token '+this.authService.getToken());
    let ep = this.endPoint.prepEndPoint('get_inodes_group/');
    return this.http.post(ep, father,{headers:headers})
  }

  unionFileGroup(info)
  {
    let headers = new Headers();
    headers.append('Content-Type','application/json');
    headers.append('Authorization','Token '+this.authService.getToken());
    let ep = this.endPoint.prepEndPoint('inode_to_group/');
    return this.http.post(ep, info,{headers:headers})
  }

}
