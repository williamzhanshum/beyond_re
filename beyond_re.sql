SELECT * from properties;
SELECT * from users;
SELECT * from tenants;
SELECT * from vendors;
SELECT * from property_has_tenant;

INSERT INTO property_has_tenant (property_id, tenant_id) VALUES (3,1);

SELECT * from properties WHERE user_id=1;
SELECT * FROM properties LEFT JOIN users on properties.user_id = 1;

-- This will get ALL the properties and its tenants for one user. 
SELECT * FROM property_has_tenant LEFT JOIN properties on properties.id = property_has_tenant.property_id LEFT JOIN tenants ON property_has_tenant.tenant_id = tenants.id WHERE user_id = 1;

SELECT * FROM property_has_tenant LEFT JOIN properties on properties.id = property_has_tenant.property_id LEFT JOIN tenants ON property_has_tenant.tenant_id = tenants.id;

SELECT * FROM property_has_tenant LEFT JOIN properties on properties.id = property_has_tenant.property_id LEFT JOIN tenants ON property_has_tenant.tenant_id = tenants.id WHERE property_id=3 and tenant_id=1; 


SELECT id from tenants ORDER BY updated_at DESC  LIMIT 1;

SELECT * FROM tenants LEFT JOIN users on users.id = tenants.user_id  WHERE tenants.id=2;

DELETE FROM property_has_tenant WHERE property_id = 3 and tenant_id= 10;

SELECT * FROM tenants LEFT JOIN users on users.id = tenants.user_id  WHERE tenants.id=4;