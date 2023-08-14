CREATE OR REPLACE FUNCTION new_rent_check()
    RETURNS TRIGGER
    AS $$
BEGIN
    IF NEW.REQUEST_STATUS = 'Accepted' AND
    EXISTS (SELECT * FROM RENT_REQUEST AS RR WHERE RR.RID = NEW.RID AND RR.GUEST_ID <> NEW.GUEST_ID AND RR.REQUEST_STATUS='Accepted' AND 
        ((NEW.START_DATE < RR.START_DATE AND NEW.END_DATE > RR.START_DATE) OR (NEW.START_DATE < RR.END_DATE AND NEW.END_DATE > RR.END_DATE))
    ) THEN
        RAISE EXCEPTION 'Two different people cannot reserve same residence same day';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER new_rent_check BEFORE INSERT OR UPDATE ON RENT_REQUEST
    FOR EACH ROW EXECUTE FUNCTION new_rent_check();
