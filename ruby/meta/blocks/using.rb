module Kernel
    def using(r)
	begin
	    yield
	ensure
	    resource.dispose
	end
    end
end
