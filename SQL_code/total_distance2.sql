--driver_insert function 
CREATE OR REPLACE FUNCTION public.total_distance3(
	data JSON)
    RETURNS JSON 
AS $BODY$

declare
	_users JSON = NULL::JSON;
    _date1 date := coalesce((data->>'date1')::date,'2000-01-01');
    _date2 date := coalesce((data->>'date2')::date,'2030-01-01');
BEGIN
	_users = (
		SELECT JSON_AGG(u) 
		FROM (
			select bus_id,sum(route.distance) as total_dis
				from trip natural join route
			where trip.date >= _date1 and trip.date<= _date2
			group by bus_id
		) u
	)::JSON;
	
	RETURN JSON_BUILD_OBJECT(
		'status', 'success',
		'users', _users
	);
END;
$BODY$
language  plpgsql;
