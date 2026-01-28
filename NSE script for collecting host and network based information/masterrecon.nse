-- Metadata and Library Imports
local http = require "http"
local stdnse = require "stdnse"
local shortport = require "shortport"

description = [[
Design a NSE script for collecting host or network based information
Metbrains Internship project for deep host reconnaissance
]]

author = "Jannatul Nayeem and Jash Vaidya"
license = "Same as Nmap"
categories = {"discovery", "safe"}

-- The Rule: Trigger on any open port
portrule = function(host, port)
  return port.state == "open"
end

-- The Action: Collecting the data
action = function(host, port)
  local gather = {}
  table.insert(gather, "Target IP " .. host.ip)

  if port.version and port.version.product then
    table.insert(gather, "Service " .. port.version.product)
    table.insert(gather, "Version " .. (port.version.version or "Unknown"))
  end

  if shortport.http(host, port) then
    local res = http.get(host, port, "/")
    if res and res.body then
      local title = string.match(res.body, "<title>(.-)</title>")
      if title then
        table.insert(gather, "Web Title " .. title)
      end
    end
    
    local rob = http.get(host, port, "/robots.txt")
    if rob and rob.status == 200 then
      table.insert(gather, "Found robots.txt file")
    end
  end

  return stdnse.format_output(true, gather)
end
