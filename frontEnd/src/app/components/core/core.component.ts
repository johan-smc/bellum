import { Component, OnInit,Input } from '@angular/core';

import { FileService } from '../../services/file.service';

@Component({
  selector: 'app-core',
  templateUrl: './core.component.html',
  styleUrls: ['./core.component.css']
})
export class CoreComponent implements OnInit {
  @Input() idGroup: string = "";
  private files : any;

  constructor(
    private fileService : FileService,
  ) {
    if( this.idGroup == "" )
      this.getFiles(null);
   }

  ngOnInit() {
  }

  getFiles(father_id)
  {
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
}
