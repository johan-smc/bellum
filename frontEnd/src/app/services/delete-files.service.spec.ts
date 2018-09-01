import { TestBed, inject } from '@angular/core/testing';

import { DeleteFilesService } from './delete-files.service';

describe('DeleteFilesService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [DeleteFilesService]
    });
  });

  it('should be created', inject([DeleteFilesService], (service: DeleteFilesService) => {
    expect(service).toBeTruthy();
  }));
});
