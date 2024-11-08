
CREATE OR REPLACE FUNCTION dashboard(_page INT, _limit INT)
RETURNS JSON AS $$
DECLARE
	_users JSON = NULL::JSON;
	_page INT = coalesce(_page, 1);
	_limit INT = coalesce(_limit, 10);
BEGIN
	_users = (
		SELECT JSON_AGG(u) 
		FROM (
			
		select bus_id,sum(distance) as total_distance, sum(oil * distance) as total_oil from 
		(	select * from 
		(		select bus_id, distance from trip natural join route) as temp1 
 		natural join bus ) as temp2 
 		natural join category group by bus_id
		ORDER BY bus_id ASC
			LIMIT _limit
			OFFSET (_page - 1) * _limit
		) u
	)::JSON;
	
	RETURN JSON_BUILD_OBJECT(
		'status', 'success',
		'data', _users
	);
END;
$$ LANGUAGE plpgsql;
