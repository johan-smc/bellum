import { Component, OnInit,Input } from '@angular/core';

import { FileService } from '../../services/file.service';
import { AuthService } from '../../services/auth.service';
import { NgFlashMessageService } from 'ng-flash-messages';


@Component({
  selector: 'app-core',
  templateUrl: './core.component.html',
  styleUrls: ['./core.component.css']
})
export class CoreComponent implements OnInit {
  @Input() idGroup: string = "";
  private files : any;
  private namefile : string;
  private namefolder : string;
  private idFather : number;

  fileToUpload: File = null;
  constructor(
    private fileService : FileService,
    private ngFlashMessageService: NgFlashMessageService,
    private authService: AuthService,
  ) {
    if( this.idGroup == "" )
      this.getFiles(null);

   }

  ngOnInit() {
  }

  getFiles(father_id)
  {
    this.idFather = father_id;
    const father = {
      father : father_id,
    }
    this.fileService.getFiles(father).subscribe(data=>{
      data = JSON.parse(data['_body']);
      this.files = data;
    });
  }
  dowloadOnClick(id)
  {
    const file = {
      id_file : id
    }
    this.fileService.getFile(file).subscribe(data=>{
      console.log(data);
      var type = data['headers']['_headers'].get('content-type')[0]
      data = data['_body'];

      var blob = new Blob([data], { type: 'plain/text' });
        // console.log(blob);
        var url= window.URL.createObjectURL(blob);
        // console.log(url);
        window.location.href = url;
    });
  }
  handleFileInput(files: FileList) {
    this.fileToUpload = files.item(0);
  }
  uploadFileToActivity() {
    this.fileService.postFile(this.fileToUpload,this.namefile,this.idFather).subscribe(data => {

      this.ngFlashMessageService.showFlashMessage({ messages:["Save file correct"], timeout : 1000, type : 'success'} );
      this.getFiles(this.idFather);
      }, error => {
        console.log(error);
      });
  }
  createFolder()
  {
    const folder={
      name : this.namefolder,
      father : this.idFather
    };
    this.fileService.createFolder(folder).subscribe(data => {

      this.ngFlashMessageService.showFlashMessage({ messages:["Save folder correct"], timeout : 1000, type : 'success'} );
      this.getFiles(this.idFather);
      }, error => {
        console.log(error);
      });
  }
  changeDate()
  {
    var dateNow = new Date();
    var dateU = new Date(this.authService.getDate());
    if( dateNow-dateU > 2629746000 )
      return true;
    return false;

  }


}
