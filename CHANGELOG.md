## 0.2.0

 - Refactor to make tap more robust.
 - Implement iterative sync for Pay Summary Report to get around 20,000 row max return limit.
 - Added fibonaccial decay backoff to the `_get()` method on all Dayforce streams.
 - Made Rollbar logging more explicitly optional.

## 0.1.1

 - Depracate `activate_version()` for `ReportStream` and instead generate a surrogate MD5 hash primary key for each received row.

## 0.1.0

 - Added in functionality to log and skip empty Employee records returned by Dayforce.