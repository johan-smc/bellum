import { TestBed, inject } from '@angular/core/testing';

import { TimeDiffService } from './time-diff.service';

describe('TimeDiffService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [TimeDiffService]
    });
  });

  it('should be created', inject([TimeDiffService], (service: TimeDiffService) => {
    expect(service).toBeTruthy();
  }));
});
