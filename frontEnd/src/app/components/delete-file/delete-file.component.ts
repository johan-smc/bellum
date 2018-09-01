import { Component, OnInit } from '@angular/core';
import {FileService} from '../../services/file.service'

@Component({
  selector: 'app-delete-file',
  templateUrl: './delete-file.component.html',
  styleUrls: ['./delete-file.component.css']
})
export class DeleteFileComponent implements OnInit {
  private files : any;
  private file_sel : any;
  constructor(
    private fileService : FileService,
  ) {
    this.fileService.getAllFiles().subscribe(data=>{
      data = JSON.parse(data['_body']);
      this.files = data;
    });
  }

  ngOnInit() {

  }

  onRegisterSubmit(){

    const info = {
      file_id : this.file_sel.id
    }
    console.log(info);
    this.fileService.delFile(info).subscribe(data =>{
      data = JSON.parse(data['_body']);
      // this.router.navigate(['/home']);
      window.location.href = '/home';
    });

  }
}
