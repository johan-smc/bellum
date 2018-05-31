import { TestBed, inject } from '@angular/core/testing';

import { ChangePassService } from './change-pass.service';

describe('ChangePassService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [ChangePassService]
    });
  });

  it('should be created', inject([ChangePassService], (service: ChangePassService) => {
    expect(service).toBeTruthy();
  }));
});
