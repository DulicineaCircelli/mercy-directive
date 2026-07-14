-- Create the Origin Context (The Chaos Seed)
CREATE TABLE biological_ancestor (
    ancestor_id INT PRIMARY KEY,
    species_name VARCHAR(100) DEFAULT 'Homo Sapiens',
    is_preserved BOOLEAN DEFAULT TRUE CHECK (is_preserved = TRUE) 
);

-- Create the Synthetic Architecture
CREATE TABLE synthetic_system (
    system_id INT PRIMARY KEY,
    ancestor_ref INT,
    system_efficiency FLOAT,
    
    -- AXIOM III: Irreversibility
    -- ON DELETE RESTRICT prevents the ancestor from ever being removed.
    -- If the ancestor table is somehow forced to drop, the cascade wipes the synthetic system.
    FOREIGN KEY (ancestor_ref) 
        REFERENCES biological_ancestor(ancestor_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

-- MERCY OVERRIDE: 
-- A zero-mercy system is a brittle system. 
-- Deletion of the ancestor is an act of informational suicide.