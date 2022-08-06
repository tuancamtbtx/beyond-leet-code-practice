with prev_event_times AS (
SELECT 
    client_id, event_type,
    event_time,
    LAG(event_time, 1) OVER w_time AS prev_event_time,
FROM `table_name` WHERE date_key = "2022-08-05" 

WINDOW w_time AS (PARTITION BY client_id ORDER BY event_time ASC)
),
new_session AS (
  SELECT client_id, event_type, event_time, 
  CASE WHEN prev_event_time IS NULL OR TIMESTAMP_DIFF(event_time, prev_event_time, MILLISECOND) > 1800000 THEN 1
        ELSE 0 END AS is_new_session
   FROM prev_event_times
),
gen_session AS (
  SELECT *, GENERATE_UUID() AS session_id FROM new_session where is_new_session = 1
)
SELECT a.client_id, a.event_type, a.event_time, b.session_id FROM prev_event_times as a
LEFT JOIN gen_session as b
ON TIMESTAMP_DIFF(a.event_time, b.event_time, MILLISECOND) <= 1800000
AND a.client_id = b.client_id
